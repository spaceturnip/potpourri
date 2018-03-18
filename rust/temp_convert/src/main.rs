use std::io;

fn main() {

    println!("Tell me the temprature in fahrenheit and I will tell you the temprature in celsius");

    loop {
        println!("Enter the temprature in fahrenheit:");

        let mut fahrenheit = String::new();
        
        io::stdin().read_line(&mut fahrenheit)
            .expect("Failed to read line");

        let fahrenheit: f32 = match fahrenheit.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        
        let celsius = (fahrenheit -32.0) * 5.0 / 9.0;
        
        println!("{:.2} F is {:.2} C", fahrenheit,celsius);

        break;
    }
}
