use serde_json::{json, Value};

pub struct Solution;

impl Solution {
    pub fn final_position_of_snake(n: i32, commands: Vec<String>) -> i32 {
        
    }
}

#[cfg(feature = "solution_3248")]
pub fn solve(input_string: String) -> Value {
	let input_values: Vec<String> = input_string.split('\n').map(|x| x.to_string()).collect();
	let n: i32 = serde_json::from_str(&input_values[0]).expect("Failed to parse input");
	let commands: Vec<String> = serde_json::from_str(&input_values[1]).expect("Failed to parse input");
	json!(Solution::final_position_of_snake(n, commands))
}
