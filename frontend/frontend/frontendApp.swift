//
//  frontendApp.swift
//  frontend
//
//  Created by June Qin on 3/2/25.
//
import Foundation
import SwiftUI

@main
struct frontendApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

let url = URL(string: "https://8ea0-2607-f010-2a7-16-a5a8-8b50-d8c6-e854.ngrok-free.app/getkit")!

let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
    guard let data = data else { return }
    print(String(data: data, encoding: .utf8)!)
}

func getBackend() async {
    print("GET STATUS")
    let url = URL(string: "https://8ea0-2607-f010-2a7-16-a5a8-8b50-d8c6-e854.ngrok-free.app/getkit")!
    var request = URLRequest(url: url)
    
    request.httpMethod = "GET"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    do {
        let (data, _) = try await URLSession.shared.data(for: request)
        
        let dataString = String(data: data, encoding: .utf8)
        print ("got data: " + dataString!)
        
    } catch {
        print("Invalid data")
        print("Error info: \(error)")
    }
    
}
