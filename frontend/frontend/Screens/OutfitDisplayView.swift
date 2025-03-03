//
//  OutfitDisplayView.swift
//  frontend
//
//  Created by June Qin on 3/2/25.
//

import SwiftUI

struct OutfitDisplayView: View {
    let bodyGrey = Color.gray.opacity(0.9)
    
    var body: some View {
        ZStack {
            VStack(spacing: 10) {
                Image("dayKit icon")
                Spacer()
                
                Rectangle()
                    .fill(bodyGrey)
                    .frame(width: 150, height: 180)
                    .overlay(Image("short sleeve").resizable().frame(width: 150, height: 180))
                
                Rectangle()
                    .fill(bodyGrey)
                    .frame(width: 150, height: 180)
                    .overlay(Image("jeans").resizable().frame(width: 150, height: 180))

                    Rectangle()
                        .fill(bodyGrey)
                        .frame(width: 70, height: 100)
                        .overlay(Image("shoes").resizable().frame(width: 150, height: 180))
                    
                Spacer()
            }
        }
    }
}

#Preview {
    OutfitDisplayView()
}
