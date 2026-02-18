use std::env;
use meval::Expr;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 4 {
        // ⚠️ .
        // mini-CAS
        print_usage();
        return;
    }

    // Interpretar limite inferior
    let a = match meval::eval_str(&args[1]) {
        Ok(val) => val,
        Err(_) => {
            println!("Erro ao interpretar limite inferior.");
            return;
        }
    };

    // Interpretar limite superior
    let b = match meval::eval_str(&args[2]) {
        Ok(val) => val,
        Err(_) => {
            println!("Erro ao interpretar limite superior.");
            return;
        }
    };

    // Converter ** para ^ (compatibilidade com meval)
    let expr_str_raw = &args[3];
    let expr_str = expr_str_raw.replace("**", "^");

    // Parse da expressão
    let expr = match expr_str.parse::<Expr>() {
        Ok(e) => e,
        Err(_) => {
            println!("Erro ao interpretar a expressão.");
            return;
        }
    };

    // Associar variável x
    let func = match expr.bind("x") {
        Ok(f) => f,
        Err(_) => {
            println!("Erro ao associar variável x.");
            return;
        }
    };

    // Número de subdivisões (é exigido par)
    let n = 1000;

    let result = integrate_simpson(&func, a, b, n);

    println!(
        "∫[{}, {}] {} dx ≈ {}",
        a, b, expr_str_raw, result
    );
}

fn integrate_simpson<F>(f: &F, a: f64, b: f64, mut n: usize) -> f64
where
    F: Fn(f64) -> f64,
{
    if n % 2 != 0 {
        n += 1;
    }

    let h = (b - a) / n as f64;
    let mut sum = f(a) + f(b);

    for i in 1..n {
        let x = a + i as f64 * h;
        if i % 2 == 0 {
            sum += 2.0 * f(x);
        } else {
            sum += 4.0 * f(x);
        }
    }

    sum * h / 3.0
}

fn print_usage() {
    println!("Uso:");
    println!("newton <a> <b> <expressao>");
    println!("Exemplo:");
    println!("newton 0 1 \"2*x^3\"");
    println!("newton 0 1 \"2*x**3\"");
}
