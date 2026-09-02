# Review Best Practices

Use this reference when reviewing code changes. Apply these criteria in addition to the automated severity rubric.

## Language-Agnostic Criteria

- **Readability:** Names reveal intent; functions are short and single-purpose.
- **Error handling:** Errors are caught, logged, and surfaced with context.
- **Input validation:** External inputs are validated before use.
- **Resource cleanup:** Files, connections, and locks are released.
- **Test coverage:** New behavior includes tests or updates existing tests.

## Security Checklist

- Injection: SQL, shell, HTML, LDAP, OS command.
- Secrets: No passwords, keys, or tokens in code or logs.
- Authentication and authorization: Checks happen before sensitive actions.
- Cryptography: Use standard libraries; avoid custom crypto.
- Dependencies: Versions pinned; no known critical CVEs introduced.

## Performance Checklist

- Algorithmic complexity: Avoid nested loops over unbounded inputs.
- Database access: Batch queries; avoid N+1 selects.
- Memory: Stream large files; avoid loading entire datasets into memory.
- Blocking calls: Offload I/O-bound work to async or background jobs.

## Framework-Specific Notes

### React
- Hooks follow rules of hooks; dependencies arrays are complete.
- State updates are immutable; keys are stable and unique.

### FastAPI
- Route handlers declare response models.
- Background tasks used for slow side effects.

### SQLAlchemy
- Sessions are scoped to request lifecycle.
- Raw SQL uses parameterized queries.
