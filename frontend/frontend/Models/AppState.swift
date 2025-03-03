//
//  AppState.swift
//  frontend
//
//  Created by Sarah Johal on 3/2/25.
//

import Foundation

enum Route: Hashable {
    case login
    case signup
}

class AppState: ObservableObject {
    @Published var routes: [Route] = []
    @Published var isAuthenticated = false

    func signOut() {
        routes = [.login]
        isAuthenticated = false
    }

}
