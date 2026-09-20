import unittest

from executor.contract import ExecutionRequest
from executor.run import run_profile


class ContractTests(unittest.TestCase):
    def test_smoke_profile_is_allowed(self):
        ExecutionRequest("smoke", "req-001").validate()

    def test_arbitrary_profile_is_rejected(self):
        with self.assertRaises(ValueError):
            ExecutionRequest("shell-anything", "req-002").validate()

    def test_request_id_is_bounded(self):
        with self.assertRaises(ValueError):
            ExecutionRequest("smoke", "bad request id").validate()

    def test_smoke_executes_without_shell(self):
        result = run_profile("smoke")
        self.assertEqual(result["exit_code"], 0)


if __name__ == "__main__":
    unittest.main()
