//
//  InputFieldView.swift
//  frontend
//
//  Created by June Qin on 3/2/25.
//

import SwiftUI

struct InputFieldView: View {
    @Binding var data: String
    
    var body: some View {
        ZStack {
            TextField("", text: $data)
              .padding(.horizontal, 10)
              .frame(width: 200, height: 42)
              .overlay(
                RoundedRectangle(cornerSize: CGSize(width: 20, height: 20))
                    .stroke(Color.white, lineWidth: 1)
                    .fill(Color.white)
              )
          }.padding(4)
    }
}

struct InputFieldView_Previews: PreviewProvider {
    @State static var data: String = ""
    
    static var previews: some View {
        InputFieldView(data: $data)
    }
}
