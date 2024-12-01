use std::fs;
use std::collections::HashMap;

fn main() {
    // day 1
    let filename = "aoc1_in.txt";
    let contents = fs::read_to_string(filename)
        .expect("file read err");
    let lines: Vec<&str> = contents.lines().collect();
    // println!("{:?}", lines);

    // puzzle 1
    let mut left: Vec<i32> = vec![];
    let mut right: Vec<i32> = vec![];
    for line in lines.iter() {
        let cols: Vec<&str> = line.split("   ").collect();
        let l: i32 = cols[0].parse().unwrap();
        let r: i32 = cols[1].parse().unwrap();
        left.push(l);
        right.push(r);
    }
    left.sort();
    right.sort();
    let mut distance: i32 = 0;
    for (i, l) in left.iter().enumerate() {
        let d = l - right[i];
        distance = distance + d.abs();
    }
    println!("{:?}", distance);

    // puzzle 2
    let mut counts = HashMap::new();
    for n in right.iter() {
        *counts.entry(n).or_insert(0) += 1;
    }
    let mut sim: i32 = 0;
    for l in left.iter() {
        sim = sim + (l * *counts.entry(l).or_insert(0));
    }
    println!("{:?}", sim);
}
