//
//  ContentView.swift
//  frontend
//
//  Created by June Qin on 3/2/25.
//

import SwiftUI

struct ContentView: View {
    
    @State private var items: [Any] = []
    /*
    func fetchData() {
        guard let url = URL(string: "https://8ea0-2607-f010-2a7-16-a5a8-8b50-d8c6-e854.ngrok-free.app/getkit") else {return}
        
        URLSession.shared.dataTask(with: url) {
            data, response, error in
            if let error = error {
                print(error)
                return
            }
            
            guard let data = data else {
                print("No data received")
                return
            }
            
            do {
                let jsonArray = try JSONSerialization.jsonObject(with: data, options: []) as? [Any]
                print(jsonArray)
            
            } catch {
                print(error)
            }
        }.resume()
        
    }
    
    var body: some View {
        VStack {
            if items.isEmpty {
                Text("fetching data")
            } else {
                Text("data fetching successful")
            }
        }.onAppear{
            fetchData()
        }
    } */

    
    var body: some View {
        LoginView()
    }
}


#Preview {
    ContentView()
}
