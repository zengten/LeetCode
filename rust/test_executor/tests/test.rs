const PROBLEM_FOLDER: &str = "problems";
const PROBLEM_ID: &str = "3145";

#[cfg(test)]
mod test {
	use solution_3145 as solution;
    use test_executor::run_test::run_test;

    use crate::{PROBLEM_FOLDER, PROBLEM_ID};

    #[test]
    fn test_solution() {
        run_test(PROBLEM_ID, PROBLEM_FOLDER, solution::solve);
    }
}
