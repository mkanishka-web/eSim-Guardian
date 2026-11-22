

def calculate_health():

    score = 100
    issues = []

    try:
        import psutil

        # Check CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)

        if cpu_usage > 80:
            score -= 20
            issues.append("High CPU usage")

        # Check RAM usage
        ram_usage = psutil.virtual_memory().percent

        if ram_usage > 80:
            score -= 20
            issues.append("High RAM usage")

        # Check disk usage
        disk_usage = psutil.disk_usage("/").percent

        if disk_usage > 90:
            score -= 20
            issues.append("Low disk space")

    except Exception as error:
        print("Health check error:", error)
        return 0

    score = max(0, score)

    print("\n===== SYSTEM HEALTH REPORT =====")
    print("Health Score:", score, "/100")

    if score >= 80:
        print("Status: Excellent")
    elif score >= 60:
        print("Status: Good")
    elif score >= 40:
        print("Status: Average")
    else:
        print("Status: Poor")

    if issues:
        print("\nIssues Found:")
        for issue in issues:
            print("-", issue)
    else:
        print("No major system issues found.")

    return score
