//
//  LoginView.swift
//  frontend
//
//  Created by June Qin on 3/2/25.
//

import SwiftUI

struct LoginView: View {
    @EnvironmentObject private var model: dayKitModel
    @EnvironmentObject private var appState: AppState

    @State private var username: String = ""
    @State private var password: String = ""
    @State private var errorMessage: String = ""
    
    private var isFormValid: Bool {
            !username.isEmpty && !password.isEmpty && (password.count >= 6 && password.count <= 10)
        }
        
        private func logIn() async {
            do {
                let response = try await model.login(username: username, password: password)
                if response.error == true {
                    errorMessage = response.reason ?? "Login failed"
                } else {
                    // appState.routes.append(.OutfitDisplayView)
                }
            } catch {
                errorMessage = error.localizedDescription
            }
        }
    
    let bodyBlue = Color.blue.opacity(0.7)
    
    var body: some View {
        VStack{
            Text("get started!")
              .font(
                Font.custom("Nunito", size: 48)
                  .weight(.black)
              )
              .foregroundColor(.black)
            ZStack {
                Rectangle()
                    .overlay(
                        VStack{
                            Text("login:")
                                .font(
                                    Font.custom("Nunito", size: 36)
                                        .weight(.black)
                                )
                                .foregroundColor(.white)
                                .padding(.vertical, 10)
                            VStack{
                                Text("username:")
                                    .font(
                                        Font.custom("Nunito", size: 20)
                                            .weight(.heavy)
                                    )
                                    .foregroundColor(.white)
                                    .frame(width: 163, alignment: .topLeading)
                                ZStack {
                                    TextField("", text: $username)
                                      .padding(.horizontal, 10)
                                      .frame(width: 200, height: 42)
                                      .overlay(
                                        RoundedRectangle(cornerSize: CGSize(width: 20, height: 20))
                                            .stroke(Color.white, lineWidth: 1)
                                            .fill(Color.white)
                                      )
                                      .textInputAutocapitalization(.never)
                                  }.padding(4)
                            }
                            .padding(.vertical, 5)
                            VStack{
                                Text("password:")
                                    .font(
                                        Font.custom("Nunito", size: 20)
                                            .weight(.heavy)
                                    )
                                    .foregroundColor(.white)
                                    .frame(width: 163, alignment: .topLeading)
                                ZStack {
                                    SecureField("", text: $password)
                                      .padding(.horizontal, 10)
                                      .frame(width: 200, height: 42)
                                      .overlay(
                                        RoundedRectangle(cornerSize: CGSize(width: 20, height: 20))
                                            .stroke(Color.white, lineWidth: 1)
                                            .fill(Color.white)
                                      )
                                  }.padding(4)
                            }
                            .padding(.vertical, 5)
                            
                            if !errorMessage.isEmpty {
                                        Text(errorMessage)
                                            .foregroundColor(.red)
                                            .font(.subheadline)
                                            .padding(.top, 8)
                                    }
                            
                            Button(action: {Task {
                                await logIn()
                            }}) {
                                Text("submit")
                                    .font(
                                        Font.custom("Nunito", size: 20)
                                            .weight(.heavy)
                                    )
                                    .foregroundColor(.black)
                            }
                            .foregroundColor(.white)
                            .frame(width: 85, height: 32)
                            .background(Color(red: 0.85, green: 0.85, blue: 0.85))
                            .cornerRadius(50)
                            .padding(.vertical, 20)
                                
                            VStack{
                                Text("no account?")
                                    .font(
                                        Font.custom("Nunito", size: 24)
                                            .weight(.heavy)
                                    )
                                    .foregroundColor(.white)
                                Rectangle()
                                    .overlay(
                                        Text("sign up")
                                            .font(
                                                Font.custom("Nunito", size: 20)
                                                    .weight(.heavy)
                                            )
                                            .foregroundColor(.black)
                                    )
                                    .foregroundColor(.white)
                                    .frame(width: 85, height: 32)
                                    .background(Color(red: 0.85, green: 0.85, blue: 0.85))
                                    .cornerRadius(50)
                                    .padding(.vertical, 10)
                            }
                            .padding(.vertical, 20)
                        }
                    )
                    .foregroundColor(.clear)
                    .frame(width: 300, height: 600)
                    .background(Color(red: 0.27, green: 0.76, blue: 0.89))
                
                Image("dayKit icon")
            }
            .frame(width: 300, height: 600)
            .background(.white)
        }
    }
}

#Preview {
    NavigationStack {
        LoginView()
            .environmentObject(dayKitModel())
            .environmentObject(AppState())
    }
}
