# API Security Fix - weather.py

## Real-World Consequences of Exposed API Keys

1. **$100K+ AWS bills**: Attackers make millions of API calls
2. **Data breaches**: Access to sensitive endpoints (weather + patient data)
3. **Account suspension**: OpenWeatherMap bans accounts immediately
4. **Legal liability**: Company violates data protection laws

## Privacy Policy: No City Logging

India's DPDP Act 2023 mandates data minimization (Section 8). City names = patient locations = PII. Logging creates unnecessary data retention risks and audit trail violations.

