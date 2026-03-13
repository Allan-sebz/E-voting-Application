# National E-Voting System - Complete Testing Guide

A step-by-step walkthrough to test the entire application UI from start to finish.

---

## 🚀 Starting the Application

```bash
cd c:\Users\DELL\Desktop\E-voting-App
python run_evoting.py
```

You'll see the ASCII art banner for "NATIONAL E-VOTING SYSTEM" and the main menu.

---

## 📋 Main Menu Options

```
1. Administrator Login
2. Voter Login
3. Register as New Voter
0. Exit System
```

---

## PART 1: ADMINISTRATOR SETUP

### Step 1: Log in as Admin

1. Select **Option 1** (Administrator Login)
2. Enter credentials:
   - **Username:** `admin`
   - **Password:** `admin123`
3. You'll see: "Welcome, System Administrator!" with role "super_admin"
4. Press Enter to continue to the Admin Dashboard

---

### Step 2: Create a Voting Station

Before voters can register, you need at least one voting station.

1. From Admin Dashboard, select **Option 10** (Create Voting Station)
2. Fill in the details:
   ```
   Station Name: Central Polling Station
   Location/Address: 123 Main Street, Kampala
   Region/District: Central
   Voter Capacity: 500
   Station Supervisor Name: John Mukasa
   Contact Phone: +256700123456
   Opening Time: 07:00
   Closing Time: 17:00
   ```
3. You'll see: "Voting Station 'Central Polling Station' created! ID: 1"

**Verify:** Select **Option 11** (View All Stations) to see your station listed.

---

### Step 3: Create a Position

Positions are the offices/roles candidates compete for.

1. Select **Option 14** (Create Position)
2. Fill in:
   ```
   Position Title: President
   Description: Head of State and Government
   Level (National/Regional/Local): National
   Number of seats/winners: 1
   Term length in years: 5
   Minimum candidate age: 35
   Key Responsibilities: Lead the nation, represent Uganda internationally
   ```
3. You'll see: "Position 'President' created! ID: 1"

**Verify:** Select **Option 15** (View All Positions) to confirm.

---

### Step 4: Create Candidates

You need candidates to compete in elections.

#### Candidate 1:
1. Select **Option 1** (Create Candidate)
2. Fill in:
   ```
   Full Name: Robert Kyagulanyi
   National ID: NIN123456789A
   Date of Birth: 1982-02-12
   Gender: M
   Education Level: Select 1 (Bachelor's Degree)
   Political Party: NUP
   Brief Manifesto: Transform Uganda through youth empowerment and economic reform
   Address: Magere, Wakiso
   Phone: +256700111222
   Email: bobi@example.com
   Has Criminal Record?: no
   Years of Public Service: 5
   ```
3. You'll see: "Candidate 'Robert Kyagulanyi' created successfully! ID: 1"

#### Candidate 2:
1. Select **Option 1** again
2. Fill in:
   ```
   Full Name: Yoweri Museveni
   National ID: NIN987654321B
   Date of Birth: 1944-09-15
   Gender: M
   Education Level: Select 2 (Master's Degree)
   Political Party: NRM
   Brief Manifesto: Continue economic development and stability
   Address: Rwakitura, Kiruhura
   Phone: +256700333444
   Email: ym@example.com
   Has Criminal Record?: no
   Years of Public Service: 40
   ```

**Verify:** Select **Option 2** (View All Candidates) to see both candidates.

---

### Step 5: Create a Poll/Election

1. Select **Option 18** (Create Poll)
2. Fill in:
   ```
   Poll/Election Title: 2026 Presidential Election
   Description: General election for President of Uganda
   Election Type: General
   Start Date: 2026-03-12
   End Date: 2026-03-15
   ```
3. You'll see available positions - enter: `1` (for President)
4. When asked "Use all active stations? (yes/no)": `yes`
5. You'll see: "Poll '2026 Presidential Election' created! ID: 1"
   - Status will be **DRAFT**

**Verify:** Select **Option 19** (View All Polls) to see your poll.

---

### Step 6: Assign Candidates to the Poll

1. Select **Option 23** (Assign Candidates to Poll)
2. Enter Poll ID: `1`
3. For "Position: President", you'll see available candidates
4. When asked "Modify candidates for President?": `yes`
5. Enter Candidate IDs: `1, 2` (comma-separated)
6. You'll see: "2 candidate(s) assigned."

---

### Step 7: Open the Poll

1. Select **Option 22** (Open / Close Poll)
2. Enter Poll ID: `1`
3. When asked "Open poll '2026 Presidential Election'?": `yes`
4. You'll see: "Poll '2026 Presidential Election' is now OPEN for voting!"

---

### Step 8: Logout from Admin

1. Select **Option 0** (Logout)
2. You'll return to the Main Menu

---

## PART 2: VOTER REGISTRATION & VOTING

### Step 9: Register as a New Voter

1. From Main Menu, select **Option 3** (Register as New Voter)
2. Fill in:
   ```
   Full Name: Jane Nakamya
   National ID Number: NIN555666777C
   Date of Birth: 1995-06-20
   Gender: F
   Residential Address: Plot 45, Ntinda, Kampala
   Phone Number: +256700555666
   Email Address: jane@example.com
   Create Password: voter123
   Confirm Password: voter123
   ```
3. You'll see available voting stations - enter: `1`
4. You'll receive:
   ```
   Registration successful!
   Your Voter Card Number: VC-XXXXXXXX (12 characters)
   IMPORTANT: Save this number! You need it to login.
   Your registration is pending admin verification.
   ```

** WRITE DOWN YOUR VOTER CARD NUMBER!**

---

### Step 10: Verify the Voter (Admin)

The voter needs verification before voting.

1. Select **Option 1** (Administrator Login)
2. Login: `admin` / `admin123`
3. Select **Option 7** (Verify Voter)
4. You'll see Jane Nakamya listed as unverified
5. Select **Option 2** (Verify all pending voters)
6. You'll see: "1 voters verified!"
7. Logout (**Option 0**)

---

### Step 11: Login as Voter

1. From Main Menu, select **Option 2** (Voter Login)
2. Enter:
   - **Voter Card Number:** (the one you saved from registration)
   - **Password:** `voter123`
3. You'll see: "Welcome, Jane Nakamya!"

---

### Step 12: View Open Polls

1. From Voter Dashboard, select **Option 1** (View Open Polls)
2. You'll see:
   ```
   Poll #1: 2026 Presidential Election [NOT YET VOTED]
   Type: General │ Period: 2026-03-12 to 2026-03-15
   
   ▸ President
     • Robert Kyagulanyi (NUP) │ Age: 44 │ Edu: Bachelor's Degree
     • Yoweri Museveni (NRM) │ Age: 81 │ Edu: Master's Degree
   ```

---

### Step 13: Cast Your Vote! 

1. Select **Option 2** (Cast Vote)
2. Select Poll ID: `1`
3. For "President" position, you'll see:
   ```
   1. Robert Kyagulanyi (NUP)
      Age: 44 │ Edu: Bachelor's Degree │ Exp: 5 yrs
      Transform Uganda through youth empowerment...
   
   2. Yoweri Museveni (NRM)
      Age: 81 │ Edu: Master's Degree │ Exp: 40 yrs
      Continue economic development and stability...
   
   0. Abstain / Skip
   ```
4. Enter your choice: `1` (or `2`, or `0` to abstain)
5. Review your vote summary
6. Confirm: `yes`
7. You'll see:
   ```
   Your vote has been recorded successfully!
   Vote Reference: VOTE-XXXXXXXX
   Thank you for participating in the democratic process!
   ```

---

### Step 14: View Voting History

1. Select **Option 3** (View My Voting History)
2. You'll see the poll you voted in and your selections

---

### Step 15: View My Profile

1. Select **Option 5** (View My Profile)
2. You'll see all your details including:
   - Voter Card Number
   - Station assignment
   - Verification status
   - Number of polls voted in

---

### Step 16: Logout

1. Select **Option 0** (Logout)
2. Return to Main Menu

---

## PART 3: VIEW RESULTS (Admin)

### Step 17: Check Election Results

1. Login as admin again
2. Select **Option 24** (View Poll Results)
3. Enter Poll ID: `1`
4. You'll see a bar chart visualization:
   ```
   President
   1. Robert Kyagulanyi (NUP)
      ██████████████████████████████████████████████████ 1 votes (100.0%)
   ```

---

### Step 18: View System Statistics

1. Select **Option 26** (System Statistics)
2. You'll see comprehensive stats:
   - Total candidates, voters, polls, stations
   - Verified vs unverified voters
   - Poll status breakdown
   - Voter turnout
   - Demographics (gender distribution)
   - Voters by station (visual bars)
   - Candidates by party

---

### Step 19: View Audit Log

1. Select **Option 31** (View Audit Log)
2. Choose **Option 1** (View all)
3. You'll see a complete trail of all actions:
   - Logins/logouts
   - Candidate creations
   - Voter registrations
   - Votes cast
   - Poll state changes

---

##  Additional Features to Explore

### Admin Dashboard (All 32 Options)

| Category | Options |
|----------|---------|
| **Candidate Management** | 1-5: Create, View, Update, Delete, Search |
| **Voter Management** | 6-9: View, Verify, Deactivate, Search |
| **Station Management** | 10-13: Create, View, Update, Delete |
| **Position Management** | 14-17: Create, View, Update, Delete |
| **Poll Management** | 18-23: Create, View, Update, Delete, Open/Close, Assign Candidates |
| **Results & Reports** | 24-27: Poll Results, By Station, Statistics, Turnout |
| **Administration** | 28-32: Create Admin, View Admins, Deactivate, Audit Log, Export |

### Voter Dashboard (6 Options)

| Option | Function |
|--------|----------|
| 1 | View Open Polls - See available elections |
| 2 | Cast Vote - Submit your ballot |
| 3 | My Voting History - See past votes |
| 4 | Election Results - View closed poll results |
| 5 | My Profile - View account details |
| 6 | Change Password |

---

##  Important Business Rules

1. **Candidate Age:** Must be 25-75 years old
2. **Voter Age:** Must be 18+ years old
3. **Criminal Record:** Candidates with criminal records are rejected
4. **Verification:** Voters must be verified before voting
5. **One Vote Per Poll:** Cannot vote twice in the same election
6. **Station Assignment:** Voters can only vote at their registered station
7. **Poll Status:**
   - Draft → Open (requires candidates assigned)
   - Open → Closed (no more votes)
   - Closed → Can be reopened

---

##  Quick Test Sequence

```
1. Admin Login (admin/admin123)
2. Create Station (Option 10)
3. Create Position (Option 14)
4. Create 2 Candidates (Option 1, twice)
5. Create Poll (Option 18)
6. Assign Candidates (Option 23)
7. Open Poll (Option 22)
8. Logout (Option 0)

9. Register Voter (Option 3 from main menu)
10. Admin Login → Verify Voter (Option 7)
11. Logout

12. Voter Login (Option 2)
13. Cast Vote (Option 2)
14. View History (Option 3)
15. Logout

16. Admin Login → View Results (Option 24)
17. View Statistics (Option 26)
```

---

##  Data Persistence

All data is saved to `evoting_data.json` in the workspace root. The file is auto-created on first run with a default admin account.

To reset the application, delete `evoting_data.json` and restart.

---

**Happy Testing! **
