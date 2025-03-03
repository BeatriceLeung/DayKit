//
//  LoginView.swift
//  frontend
//
//  Created by June Qin on 3/2/25.
//

import SwiftUI

struct LoginView: View {
    let bodyBlue = Color.blue.opacity(0.7)
    @State var username: String = ""
    @State var password: String = ""
    
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
                                InputFieldView(data: $username)
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
                                InputFieldView(data: $password)
                            }
                            .padding(.vertical, 5)
                            Rectangle()
                                .overlay(
                                    Text("submit")
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
                
            }
            .frame(width: 300, height: 600)
            .background(.white)
        }
    }
}

#Preview {
    LoginView()
}
