# requisitionsystem.py
# Simple Level 3-4 Requisition System

class RequisitionSystem:
    def __init__(self):
        # Shared data
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = 0
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"

    # a. Staff info
    def staff_info(self):
        print("\n--- Enter Staff Information ---")
        self.date = input("Enter Date (DD/MM/YYYY): ")
        self.staff_id = input("Enter Staff ID: ")
        self.staff_name = input("Enter Staff Name: ")
        try:
            self.requisition_id = int(input("Enter Requisition ID: "))
        except:
            self.requisition_id = 0

    # b. Requisition details
    def requisitions_details(self):
        print("\n--- Enter Requisition Details ---")
        try:
            self.total = float(input("Enter Total Amount ($): "))
        except:
            self.total = 0

    # c. Requisition approval
    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref = self.staff_id + str(self.requisition_id)
        elif self.total <= 1000:
            self.status = "Pending"
            self.approval_ref = "Not available"
        else:
            self.status = "Not approved"
            self.approval_ref = "Not available"

    # d. Manager response
    def respond_requisition(self):
        if self.status == "Pending":
            print("\nThis requisition is pending.")
            answer = input("Manager, enter decision (approve/reject/skip): ").lower()
            if answer == "approve":
                self.status = "Approved"
                self.approval_ref = self.staff_id + str(self.requisition_id)
            elif answer == "reject":
                self.status = "Not approved"
                self.approval_ref = "Not available"
            else:
                print("No changes made.")
        else:
            print("Requisition is not pending, no response needed.")

    # e. Display requisition
    def display_requisition(self):
        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference:", self.approval_ref)


# f. Statistics (very simple)
def show_statistics(requisitions):
    total = len(requisitions)
    approved = 0
    pending = 0
    not_approved = 0

    for r in requisitions:
        if r.status == "Approved":
            approved = approved + 1
        elif r.status == "Pending":
            pending = pending + 1
        else:
            not_approved = not_approved + 1

    print("\n=== Requisition Statistics ===")
    print("Total Requisitions:", total)
    print("Approved:", approved)
    print("Pending:", pending)
    print("Not Approved:", not_approved)


# -------------------------------
# Testing the program
# -------------------------------
all_requisitions = []

print("=== SIMPLE REQUISITION SYSTEM ===")

# Create at least 5 requisitions
for i in range(5):
    print("\n--- Requisition", i + 1, "---")
    r = RequisitionSystem()
    r.staff_info()
    r.requisitions_details()
    r.requisition_approval()
    all_requisitions.append(r)

# Show all requisitions before manager response
print("\n--- All Requisitions (Before Manager Response) ---")
for r in all_requisitions:
    r.display_requisition()

show_statistics(all_requisitions)

# Manager responds to pending
print("\n--- Manager Responds to Pending Requisitions ---")
for r in all_requisitions:
    if r.status == "Pending":
        r.respond_requisition()

# Show all again after manager decisions
print("\n--- All Requisitions (After Manager Response) ---")
for r in all_requisitions:
    r.display_requisition()

show_statistics(all_requisitions)

