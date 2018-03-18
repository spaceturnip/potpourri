fn main() {
    let days = [
        "first", 
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ];

    let gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,\nand",
        "Three french hens,",
        "Four calling birds,",
        "FIIIIIIIVE GOOOOOOOOOLDEEEEEEEN RIIIIIIINGS!",
        "Six geese a laying,",
        "Seven swans a swimming,",
        "Eight maids a milking,",
        "Nine ladies dancing,",
        "Ten lords a leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ];


    for day in 0..12 {
        println!("On the {} day of Christmas, my true love sent to me:", 
                 days[day]);
        for gift in (0..day+1).rev() {
            println!("{}", gifts[gift]);
        }
        println!("");
    }
}

