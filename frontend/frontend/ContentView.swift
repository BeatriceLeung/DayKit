import SwiftUI

struct ContentView: View {
    @State private var items: [String] = []

    init() {
        // The initialization logic can be handled within the body or onAppear
    }

    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundStyle(.tint)
            Text("Hello, world!")
            ForEach(items, id: \.self) { clothing in
                Text(clothing)
            }
        }
        .padding()
        .onAppear {
            fetchData()  // Fetch data when the view appears
        }
    }

    func fetchData() {
        let url = URL(string: "https://1a14-2607-f010-2a7-16-a5a8-8b50-d8c6-e854.ngrok-free.app/getkit")

        URLSession.shared.dataTask(with: url!) { data, response, error in
            if let error = error {
                print(error)
                return
            }

            if let data = data {
                do {
                    // Parse the JSON response and update the state variable
                    let jsonArray = try JSONSerialization.jsonObject(with: data, options: []) as? [String]
                    DispatchQueue.main.async {
                        items = jsonArray ?? []  // Update the state variable on the main thread
                    }
                } catch {
                    print(error)
                }
            }
        }.resume()
    }
}

#Preview {
    ContentView()
}
