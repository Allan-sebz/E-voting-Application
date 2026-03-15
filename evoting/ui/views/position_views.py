"""
Position views - display logic for position management screens.
"""

from ..console import (
    clear_screen, header, subheader, table_header, table_divider,
    error, success, warning, info, menu_item, status_badge, prompt, pause
)
from ..colors import RESET, BOLD, DIM, THEME_ADMIN, THEME_ADMIN_ACCENT
from ...config import MIN_CANDIDATE_AGE, DEFAULT_POSITION_SEATS, DEFAULT_TERM_LENGTH_YEARS


class PositionViews:
    """Handles position-related UI rendering."""
    
    def __init__(self, position_service, data_store):
        self.position_service = position_service
        self.data_store = data_store
    
    def create_position(self, current_user):
        """Display create position form."""
        clear_screen()
        header("CREATE POSITION", THEME_ADMIN)
        print()
        
        title = prompt("Position Title: ")
        if not title:
            error("Title cannot be empty.")
            pause()
            return
        
        description = prompt("Description: ")
        
        level = prompt("Level (National/Regional/Local): ")
        if level not in ["National", "Regional", "Local"]:
            warning("Using 'Local' as default level.")
            level = "Local"
        
        try:
            max_winners = int(prompt(f"Number of seats/winners (default {DEFAULT_POSITION_SEATS}): ") or str(DEFAULT_POSITION_SEATS))
            if max_winners < 1:
                max_winners = DEFAULT_POSITION_SEATS
        except ValueError:
            max_winners = DEFAULT_POSITION_SEATS
        
        try:
            term_length = int(prompt(f"Term length in years (default {DEFAULT_TERM_LENGTH_YEARS}): ") or str(DEFAULT_TERM_LENGTH_YEARS))
        except ValueError:
            term_length = DEFAULT_TERM_LENGTH_YEARS
        
        try:
            min_age = int(prompt(f"Minimum candidate age (default {MIN_CANDIDATE_AGE}): ") or str(MIN_CANDIDATE_AGE))
        except ValueError:
            min_age = MIN_CANDIDATE_AGE
        
        responsibilities = prompt("Key Responsibilities: ")
        
        success_flag, result = self.position_service.create_position(
            title=title,
            description=description,
            level=level,
            max_winners=max_winners,
            term_length=term_length,
            min_candidate_age=min_age,
            responsibilities=responsibilities,
            created_by=current_user["username"]
        )
        
        if success_flag:
            print()
            success(f"Position '{title}' created! ID: {result}")
            self.data_store.save()
        else:
            error(result)
        pause()
    
    def view_all_positions(self):
        """Display all positions."""
        clear_screen()
        header("ALL POSITIONS", THEME_ADMIN)
        positions = self.data_store.get_all_positions()
        
        if not positions:
            print()
            info("No positions found.")
            pause()
            return
        
        print()
        table_header(
            f"{'ID':<5} {'Title':<25} {'Level':<12} {'Seats':<6} {'Min Age':<8} {'Term':<6} {'Status':<10}",
            THEME_ADMIN
        )
        table_divider(72, THEME_ADMIN)
        
        for pid, p in positions.items():
            status = status_badge("Active", True) if p["is_active"] else status_badge("Inactive", False)
            print(f"  {p['id']:<5} {p['title']:<25} {p['level']:<12} {p['max_winners']:<6} {p['min_candidate_age']:<8} {p['term_length']} yrs {status}")
        
        print(f"\n  {DIM}Total Positions: {len(positions)}{RESET}")
        pause()
    
    def update_position(self, current_user):
        """Display update position form."""
        clear_screen()
        header("UPDATE POSITION", THEME_ADMIN)
        positions = self.data_store.get_all_positions()
        
        if not positions:
            print()
            info("No positions found.")
            pause()
            return
        
        print()
        for pid, p in positions.items():
            print(f"  {THEME_ADMIN}{p['id']}.{RESET} {p['title']} {DIM}({p['level']}){RESET}")
        
        try:
            pid = int(prompt("\nEnter Position ID to update: "))
        except ValueError:
            error("Invalid input.")
            pause()
            return
        
        if pid not in positions:
            error("Position not found.")
            pause()
            return
        
        p = positions[pid]
        print(f"\n  {BOLD}Updating: {p['title']}{RESET}")
        info("Press Enter to keep current value\n")
        
        updates = {}
        
        new_title = prompt(f"Title [{p['title']}]: ")
        if new_title:
            updates["title"] = new_title
        
        new_desc = prompt(f"Description [{p['description'][:50]}]: ")
        if new_desc:
            updates["description"] = new_desc
        
        new_level = prompt(f"Level [{p['level']}]: ")
        if new_level and new_level in ["National", "Regional", "Local"]:
            updates["level"] = new_level
        
        new_winners = prompt(f"Max Winners [{p['max_winners']}]: ")
        if new_winners:
            try:
                updates["max_winners"] = int(new_winners)
            except ValueError:
                warning("Invalid number, keeping old value.")
        
        new_term = prompt(f"Term Length [{p['term_length']}]: ")
        if new_term:
            try:
                updates["term_length"] = int(new_term)
            except ValueError:
                warning("Invalid number, keeping old value.")
        
        new_age = prompt(f"Min Candidate Age [{p['min_candidate_age']}]: ")
        if new_age:
            try:
                updates["min_candidate_age"] = int(new_age)
            except ValueError:
                warning("Invalid number, keeping old value.")
        
        if updates:
            success_flag, err = self.position_service.update_position(
                pid, updates, current_user["username"]
            )
            if success_flag:
                print()
                success(f"Position '{p['title']}' updated successfully!")
                self.data_store.save()
            else:
                error(err)
        
        pause()
    
    def delete_position(self, current_user):
        """Display delete position confirmation."""
        clear_screen()
        header("DELETE POSITION", THEME_ADMIN)
        positions = self.data_store.get_all_positions()
        polls = self.data_store.get_all_polls()
        
        if not positions:
            print()
            info("No positions found.")
            pause()
            return
        
        print()
        for pid, p in positions.items():
            status = status_badge("Active", True) if p["is_active"] else status_badge("Inactive", False)
            print(f"  {THEME_ADMIN}{p['id']}.{RESET} {p['title']} {DIM}({p['level']}){RESET} {status}")
        
        try:
            pid = int(prompt("\nEnter Position ID to delete: "))
        except ValueError:
            error("Invalid input.")
            pause()
            return
        
        if pid not in positions:
            error("Position not found.")
            pause()
            return
        
        # Check if position is used in any poll
        for poll_id, poll in polls.items():
            for pos in poll.get("positions", []):
                if pos["position_id"] == pid and poll["status"] == "open":
                    error(f"Cannot delete - position is used in active poll: {poll['title']}")
                    pause()
                    return
        
        if prompt(f"Deactivate position '{positions[pid]['title']}'? (yes/no): ").lower() == "yes":
            success_flag, err = self.position_service.deactivate_position(
                pid, current_user["username"]
            )
            if success_flag:
                print()
                success(f"Position '{positions[pid]['title']}' deactivated.")
                self.data_store.save()
            else:
                error(err)
        
        pause()
