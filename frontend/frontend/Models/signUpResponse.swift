//
//  signUpResponse.swift
//  frontend
//
//  Created by Sarah Johal on 3/2/25.
//
import Foundation

struct signUpResponse: Codable {
    let error: Bool
    var reason: String? = nil
}

