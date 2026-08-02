import subprocess
import sys
import time

# Array of script
scripts = ["src/generate_logs.py", "src/process_logs.py", "src/validate_metrics.ts", "src/alert_engine.py" ]

counter = 0
# track pipeline start time
p_start_time = time.perf_counter()
print("Starting LogSentinel Pipeline...")


# traverse through the scripts
for script in scripts:
    counter = counter + 1
    # print the scripts that's running
    print(f"[{counter}/{len(scripts)}] Running {script[4:]}...", end=" ", flush=True)
    # track start time of each script
    start_time = time.perf_counter()
    try:
        # run each python scropt using sys.executable
        if (script[-2:]=='py'):
            subprocess.run([sys.executable, script], check=True)
        else:
            subprocess.run(["npx", "tsx", script], check=True, shell=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        # Print which script failed
        print(f"\nFailed (Exit Code: {e.returncode})\n")
        # print failed pipeline statement
        print(
            f"PIPELINE EXECUTION FAILED\nFailed Stage: {script}\nError: Process exited with non-zero code {e.returncode}\n"
        )
        sys.exit(1)
    end_time = time.perf_counter()
    # track runtime metrics of each script
    elapsed = end_time - start_time
    print(f"Completed in {elapsed:.2f}s")


p_end_time = time.perf_counter()
# total time duration of pipeline
p_elapsed = p_end_time - p_start_time

print(f"\nPIPELINE EXECUTION SUCCESSFUL\nTotal Duration: {p_elapsed:.1f}s ")
