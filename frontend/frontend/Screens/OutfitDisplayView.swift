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
                Spacer()
                
                Rectangle()
                    .fill(bodyGrey)
                    .frame(width: 150, height: 180)
                
                Rectangle()
                    .fill(bodyGrey)
                    .frame(width: 150, height: 180)

                HStack(spacing: 10) {
                    Rectangle()
                        .fill(bodyGrey)
                        .frame(width: 70, height: 100)
                    
                    Rectangle()
                        .fill(bodyGrey)
                        .frame(width: 70, height: 100)
                }
                Spacer()
            }
        }
    }
}

#Preview {
    OutfitDisplayView()
}
