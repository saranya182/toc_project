# ----- Malaria FSM -----
class MalariaFSM:
    def _init_(self):
        self.state = 'S0'
        self.infected_count = 0

    def transition(self, observation):
        if self.state == 'S0' and observation == 'normal_rbc':
            self.state = 'S1'
            print("State: S1 – Normal RBC detected.")
        elif self.state in ['S1', 'S2'] and observation == 'parasite_dot':
            self.infected_count += 1
            if self.infected_count < 3:
                self.state = 'S2'
                print(f"State: S2 – Infected RBC detected (Count: {self.infected_count}).")
            else:
                self.state = 'S3'
                print("State: S3 – Multiple infected RBCs detected.")
        elif self.state == 'S3' and observation == 'threshold_reached':
            self.state = 'S4'
            print("State: S4 – Malaria Detected!")
        else:
            print(f"No valid transition from state {self.state} on input '{observation}'.")

    def is_disease_detected(self):
        return self.state == 'S4'


# ----- Leukemia FSM -----
class LeukemiaFSM:
    def _init_(self):
        self.state = 'S0'
        self.large_wbc_count = 0

    def transition(self, observation):
        if self.state == 'S0' and observation == 'normal_wbc':
            self.state = 'S1'
            print("State: S1 – Normal WBC detected.")
        elif self.state in ['S1', 'S2'] and observation == 'large_wbc':
            self.large_wbc_count += 1
            if self.large_wbc_count < 5:
                self.state = 'S2'
                print(f"State: S2 – Large WBC detected (Count: {self.large_wbc_count}).")
            else:
                self.state = 'S3'
                print("State: S3 – Abnormal WBC pattern forming.")
        elif self.state == 'S3' and observation == 'high_count':
            self.state = 'S4'
            print("State: S4 – Leukemia Detected!")
        else:
            print(f"No valid transition from state {self.state} on input '{observation}'.")

    def is_disease_detected(self):
        return self.state == 'S4'


# ----- Main Program -----
def main():
    print("=== Blood Anomaly Detection FSM ===")
    print("Choose the test:")
    print("1. Malaria")
    print("2. Leukemia")
    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == '1':
        fsm = MalariaFSM()
        print("\n--- Malaria Detection ---")
        print("Enter observations: normal_rbc / parasite_dot / threshold_reached")
    elif choice == '2':
        fsm = LeukemiaFSM()
        print("\n--- Leukemia Detection ---")
        print("Enter observations: normal_wbc / large_wbc / high_count")
    else:
        print("Invalid choice.")
        return
    print("Type 'exit' to stop.")
    while True:
        obs = input("Enter observation: ").strip().lower()
        if obs == 'exit':
            break
        fsm.transition(obs)
    if fsm.is_disease_detected():
        if choice == '1':
            print("\n🦠 Result: Malaria Positive – Multiple infected RBCs detected.")
        else:
            print("\n🧬 Result: Leukemia Positive – Abnormal WBCs detected.")
    else:
        print("\n✅ Result: No disease detected based on current input.")
# Run the program
if _name_ == '_main_':
    main()