#![allow(dead_code, unused_imports)]
use std::fs::{read_to_string, File};
use std::io::{self, prelude::*, BufReader};

fn main1() {
    let file = File::open("public/input.txt").expect("error reading file");
    let reader = BufReader::new(file);
    let mut max_cal: u32 = 0;
    let mut cur_cal: u32 = 0;
    for line in reader.lines() {
        let line = line.unwrap_or("".to_string());
        match line.as_str() {
            "" => {
                cur_cal = 0;
            }
            _ => {
                cur_cal += line.parse::<u32>().unwrap();
                max_cal = max_cal.max(cur_cal);
            }
        }
    }
    println!("max_cal: {}", max_cal);
}

fn main2() {
    let contents = read_to_string("public/input.txt").expect("error reading file");
    let max_cal:u32 = contents.split("\n\n").map(|group| {
        group.lines().map(|line| {
            line.parse::<u32>().unwrap_or(0)
        }).sum()
    }).max().unwrap_or(0);
    println!("max_cal: {:?}", max_cal);

}

fn main() {
    let file = File::open("public/input.txt").expect("error reading file");
    let reader = BufReader::new(file);
    let max_cal = reader
        .lines()
        .scan(0, |sum_cal, cur_cal|{ 
            *sum_cal = match cur_cal.unwrap().parse::<u32>() {
                Ok(cal) => *sum_cal + cal,
                _ => 0,
            };
            Some(*sum_cal)
        })
        // .collect::<Vec<u32>>();
        .max()
        .unwrap_or(0);
    println!("max_cal: {:?}", max_cal);
}
