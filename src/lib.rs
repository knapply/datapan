use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

use std::{
    fs,
    io::{BufRead, BufReader},
};

use rayon::{iter::ParallelBridge, prelude::*};

fn read_lines(file_path: &str) -> Vec<String> {
    let file = fs::File::open(&file_path).expect("file not found");
    let reader = BufReader::new(file);

    reader
        .lines()
        .par_bridge()
        .map(|l| l.expect("could not parse line"))
        .collect::<Vec<String>>()
}

fn list_files(dir_path: &str) -> Vec<String> {
    let paths = fs::read_dir(dir_path).unwrap();

    paths
        .map(|entry| {
            let entry = entry.unwrap();
            let entry_path = entry.path();
            let file_name_as_str = entry_path.to_str().unwrap();
            String::from(file_name_as_str)
        })
        .collect::<Vec<String>>()
}

#[pyfunction]
fn hello_rust(target_dir: &str) -> Vec<String> {
    let mut target_files = list_files(target_dir);

    target_files
        .par_iter_mut()
        .flat_map(|f| read_lines(f))
        .collect::<Vec<String>>()
}

#[pymodule]
fn sift(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(hello_rust))?;

    Ok(())
}
