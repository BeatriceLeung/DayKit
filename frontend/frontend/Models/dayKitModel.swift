import Foundation
import SwiftUI

class dayKitModel: ObservableObject {
    @Published private var appState = AppState()
    
    func login(username: String, password: String) async throws -> loginResponse {
        let loginData = ["username": username, "password": password]
        let resource = try Resource(
            url: Constants.Urls.login,
            method: .post(JSONEncoder().encode(loginData)),
            modelType: loginResponse.self)
        
        let loginResponseDTO = try await httpClient().load(resource)
        
        if !loginResponseDTO.error,
           let token = loginResponseDTO.token,
           let userId = loginResponseDTO.userId {
            // Save the token and userId in UserDefaults
            let defaults = UserDefaults.standard
            defaults.set(token, forKey: "authToken")
            defaults.set(userId.uuidString, forKey: "userId")
            
            await MainActor.run {
                appState.isAuthenticated = true
            }
        }

        return loginResponseDTO
    }
    
    func signUp(name: String, username: String, email: String, password: String) async throws -> signUpResponse {
        let signUpData = ["name": name, "username": username, "email": email, "password": password]
        let resource = try Resource(
            url: Constants.Urls.signUp!,
            method: .post(JSONEncoder().encode(signUpData)),
            modelType: signUpResponse.self
        )
        return try await httpClient().load(resource)
    }
}

