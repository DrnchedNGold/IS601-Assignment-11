# Task Progress Checklist

- [x] Analyze requirements and current test coverage
- [x] Plan unit test cases for operation types and CalculationCreate validation
- [x] Plan integration test cases for DB operations and error scenarios
- [ ] Expand unit tests to cover all edge cases and reach 100+ total tests
- [ ] Expand integration tests to cover all DB scenarios and error cases
- [ ] Ensure integration tests use PostgreSQL via GitHub Actions workflow
- [ ] Review and verify all tests for completeness and correctness

## Planned Additional Test Cases

### Unit Tests
- [ ] Parameterized tests for all operations with various input types (int, float, negative, zero, large numbers)
- [ ] Tests for CalculationFactory with mixed-case operation names
- [ ] Tests for CalculationCreate with missing/extra fields
- [ ] Tests for CalculationCreate with invalid input types (string, None, list of lists)
- [ ] Tests for CalculationCreate with too many/few inputs
- [ ] Tests for CalculationCreate with boundary values
- [ ] Tests for CalculationFactory with unsupported types

### Integration Tests
- [ ] DB insert and retrieve for all operation types
- [ ] DB insert with invalid types/inputs
- [ ] DB transaction rollback on error
- [ ] Concurrent DB inserts
- [ ] API error responses for invalid requests
- [ ] API responses for boundary values
- [ ] API responses for large payloads
- [ ] API responses for missing fields
- [ ] API responses for invalid UUIDs
