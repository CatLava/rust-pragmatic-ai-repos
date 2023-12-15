use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn calculate_pi(iterations: u32) -> PyResult<f64> {
    let mut pi = 0.0;
    for _k in 0..iterations {
        pi += 1f64
    }
    Ok(pi)
}

/// A Python module implemented in Rust.
#[pymodule]
fn python_pi(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_pi, m)?)?;
    Ok(())
}
