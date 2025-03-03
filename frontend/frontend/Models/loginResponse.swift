//
//  loginResponse.swift
//  frontend
//
//  Created by Sarah Johal on 3/2/25.
//

import Foundation

struct loginResponse: Codable {
    let error: Bool
    var reason: String? = nil
    var token: String? = nil
    var userId: UUID? = nil
}
