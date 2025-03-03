//
//  Constants.swift
//  frontend
//
//  Created by Sarah Johal on 3/2/25.
//

import Foundation

struct Constants {
    private static let baseUrlPath = "https://1a14-2607-f010-2a7-16-a5a8-8b50-d8c6-e854.ngrok-free.app"
    
    struct Urls {
        static let login = URL(string: "\(baseUrlPath)/login")!
        static let signUp = URL(string: "\(baseUrlPath)/signUp")
    }
}
