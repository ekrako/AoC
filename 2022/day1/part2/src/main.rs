#![allow(unused_imports, dead_code)]
use std::fs::{File, read_to_string};
use std::io::{prelude::*, BufReader};
use std::cmp::Ordering;


// in memory implementation with reverse iterator
fn in_memroy_with_reverse_iter() {
    let contents = read_to_string("input.txt").expect("error reading file");
    let mut all_cal = contents.split("\n\n").map(|group| {
        group.lines().map(|line| {
            line.parse::<u32>().unwrap_or(0)
        }).sum()
    }).collect::<Vec<u32>>();
    all_cal.sort();
    println!("all_cal: {:?}", all_cal);
    let max_cal: u32 = all_cal.iter().rev().take(3).sum();
    println!("max_cal: {:?}", max_cal);
}

// in memory implementation with reverse sort
fn in_memroy_with_reverse_sort() {
    let contents = read_to_string("input.txt").expect("error reading file");
    let mut all_cal = contents.split("\n\n").map(|group| {
        group.lines().map(|line| {
            line.parse::<u32>().unwrap_or(0)
        }).sum()
    }).collect::<Vec<u32>>();
    all_cal.sort_by(|a, b| b.cmp(a));
    println!("all_cal: {:?}", all_cal);
    let max_cal: u32 = all_cal.iter().take(3).sum();
    println!("max_cal: {:?}", max_cal);
}

// iterator implementation with max_cal as vector
fn iterable_with_max_cal_by() {
    let file = File::open("input.txt").expect("error reading file");
    let reader = BufReader::new(file);
    let mut cur_cal: u32 = 0;
    let mut max_cal = vec![0;3];
    for line in reader.lines() {
        let line = line.unwrap_or("".to_string());
        match line.as_str() {
            "" => {
                max_cal = save_max_cal(max_cal, cur_cal);
                cur_cal = 0;
            }
            _ => {
                cur_cal += line.parse::<u32>().unwrap();
            }
        }
    }
    max_cal = save_max_cal(max_cal, cur_cal);
    println!("max_cal: {:?}", max_cal);
}

fn save_max_cal(mut max_cal:Vec<u32>,cur_cal:u32) -> Vec<u32> {
    let (min_max_cal_index, min_max_cal) = max_cal.iter().enumerate().min_by(|(_,a),(_,b)| a.cmp(b)).unwrap();
    max_cal[min_max_cal_index] = cur_cal.max(*min_max_cal);
    max_cal
}
// iterable solution with max_cal as Box<[u32;3]>
fn iter_with_box() {
    let file = File::open("input.txt").expect("error reading file");
    let reader = BufReader::new(file);
    let mut cur_cal: u32 = 0;
    let mut max_cal: Box<[u32;3]> = Box::new([0;3]);
    for line in reader.lines() {
        let line = line.unwrap_or("".to_string());
        match line.as_str() {
            "" => {
                max_cal = save_max_cal_c(max_cal, cur_cal);
                cur_cal = 0;
            }
            _ => {
                cur_cal += line.parse::<u32>().unwrap();
            }
        }
    }
    max_cal = save_max_cal_c(max_cal, cur_cal);
    println!("max_cal: {}", max_cal.iter().sum::<u32>());
}

fn save_max_cal_c(mut max_cal:Box<[u32;3]>,cur_cal:u32)-> Box<[u32;3]> {
    let (min_max_cal_index, min_max_cal) = max_cal.iter().enumerate().min_by(|(_,a),(_,b)| a.cmp(b)).unwrap();
    max_cal[min_max_cal_index] = cur_cal.max(*min_max_cal);
    max_cal
}

// iterable solution with max_cal as [u32;3] passed by reference 
fn main() {
    let file = File::open("input.txt").expect("error reading file");
    let reader = BufReader::new(file);
    let mut cur_cal: u32 = 0;
    let mut max_cal: [u32;3] = [0;3];
    for line in reader.lines() {
        let line = line.unwrap_or("".to_string());
        match line.as_str() {
            "" => {
                save_max_cal_b(&mut max_cal, cur_cal);
                cur_cal = 0;
            }
            _ => {
                cur_cal += line.parse::<u32>().unwrap();
            }
        }
    }
    save_max_cal_b(&mut max_cal, cur_cal);
    println!("max_cal: {}", max_cal.iter().sum::<u32>());
}

fn save_max_cal_b(max_cal:&mut [u32;3],cur_cal:u32)  {
    let (min_max_cal_index, min_max_cal) = max_cal.iter().enumerate().min_by(|(_,a),(_,b)| a.cmp(b)).unwrap();
    // max_cal[min_max_cal_index] = cur_cal.max(*min_max_cal);
    if cur_cal > *min_max_cal {
        max_cal[min_max_cal_index] = cur_cal;
    }
}
// max_cal: 198551