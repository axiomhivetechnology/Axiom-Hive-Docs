# Error Catalog

Common bug patterns detected in pull request diffs. Each entry includes detection guidance and a suggested fix.

## Security

### Hardcoded Secret
- **Why it matters:** Credentials in source code leak through version history.
- **Detection:** Look for strings matching password, secret, api_key, token, followed by `=` or string literals.
- **Fix:** Move to environment variables or a secrets manager.

### SQL Injection via Concatenation
- **Why it matters:** Untrusted input alters query structure.
- **Detection:** Search for `+` or f-strings inside SQL execution calls.
- **Fix:** Use parameterized queries or ORM filters.

### Unvalidated Redirect
- **Why it matters:** Attackers can redirect users to phishing sites.
- **Detection:** Look for redirect calls using request parameters without allowlist.
- **Fix:** Validate redirect URLs against an allowlist.

## Logic

### Off-by-One in Loop
- **Why it matters:** Skips last element or reads past bounds.
- **Detection:** Check range endpoints, `<=` vs `<`, zero-based indexing.
- **Fix:** Use inclusive start, exclusive end convention; add boundary tests.

### Mutable Default Argument
- **Why it matters:** Shared state across function calls causes subtle bugs.
- **Detection:** Search for `def func(x=[]):` or `{}` default literals.
- **Fix:** Use `None` and initialize inside the function.

### Race Condition on Shared State
- **Why it matters:** Concurrent writes corrupt data.
- **Detection:** Look for module-level mutation inside async handlers or threads.
- **Fix:** Use locks, queues, or atomic operations.

## Performance

### N+1 Query
- **Why it matters:** Database hit count grows linearly with result set.
- **Detection:** Look for loops containing database or API calls per item.
- **Fix:** Batch fetch with `WHERE id IN (...)` or eager loading.

### Large Object in Memory
- **Why it matters:** Memory pressure and GC pauses.
- **Detection:** Search for `read()`, `readlines()`, or `json.load` on large files.
- **Fix:** Stream with generators or chunked readers.

### Blocking Call in Async Context
- **Why it matters:** Blocks event loop; stalls all concurrent requests.
- **Detection:** Look for `time.sleep`, synchronous HTTP calls, or CPU-heavy work in async functions.
- **Fix:** Use `asyncio.sleep`, async HTTP client, or background task queue.

## Style

### Deeply Nested Conditional
- **Why it matters:** Reduces readability and increases defect rate.
- **Detection:** Count nested `if`/`else` depth greater than 3.
- **Fix:** Use early returns, guard clauses, or polymorphism.

### Magic Number
- **Why it matters:** Hides intent and makes maintenance error-prone.
- **Detection:** Search for numeric literals outside of constants or configs.
- **Fix:** Extract to named constant with domain meaning.

### Missing Docstring on Public Function
- **Why it matters:** Consumers cannot discover behavior or constraints.
- **Detection:** Look for `def` or `function` without adjacent docstring or comment block.
- **Fix:** Add docstring describing purpose, args, returns, and raises.
