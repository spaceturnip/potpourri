use std::io;

fn main() {

    println!("Tell me which fibonacci number to find.");

    let mut num = String::new();

    io::stdin().read_line(&mut num)
        .expect("Unable to read line.");

    let num: u64 = num.trim().parse()
        .expect("Enter a number!");

    println!("The {}th fibonacci number is {}.", num, fib(num));

}

fn fib(n: u64) -> u64 {

    if n <= 2 {
        return 1;
    } else {
        return fib(n - 2) + fib(n - 1);
    }
}

