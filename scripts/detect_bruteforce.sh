#!/bin/bash

LOG_FILE="../logs/auth.log"
ALERT_FILE="../logs/alerts.log"

THRESHOLD=3

tail -n 50 "$LOG_FILE" | grep "FAILED" | awk '{print $5}' | sort | uniq -c | while read count ip
do
    if [ "$count" -ge "$THRESHOLD" ]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') | ALERT | Brute-force detected from $ip" >> "$ALERT_FILE"
    fi
done
