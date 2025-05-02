# index.py
# Entry point for the AI-Enhanced MFA experiment

import os

def run_script(script_name):
    print(f"\n▶️ Running {script_name}...")
    exit_code = os.system(f"python {script_name}")
    if exit_code != 0:
        print(f"❌ Error occurred while running {script_name}. Exiting.")
        exit(1)

def main():
    print("🔐 AI-Enhanced MFA Experiment: Pipeline Start\n")

    # Step 1: Generate synthetic datasets
    run_script("generate_uald.py")
    run_script("generate_abbd.py")

    # Step 2: Simulate academic workflows and attack scenarios
    run_script("simulate_workflows.py")

    # Step 3: Preprocess and feature engineer datasets
    run_script("preprocess.py")

    # Step 4: Train machine learning models
    run_script("train_models.py")

    # Step 5: Evaluate system performance and visualize metrics
    run_script("evaluate.py")

    print("\n✅ All steps completed. Outputs saved in the /data folder.")

if __name__ == "__main__":
    main()
