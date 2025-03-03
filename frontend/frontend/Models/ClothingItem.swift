//
//  Clothing.swift
//  frontend
//
//  Created by June Qin on 3/2/25.
//

import Foundation

struct ClothingItem: Codable, Identifiable {
    let id: UUID
    let name: String
    let type: String
}
