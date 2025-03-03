//
//  Outfit.swift
//  frontend
//
//  Created by June Qin on 3/2/25.
//

import Foundation

struct Outfit: Codable {
    let top: ClothingItem
    let layers_top: Int
    let jacket: Bool
    let bottom: ClothingItem
    let layers_bottom: Int
    let socks: ClothingItem
    let shoes: ClothingItem
    
}
