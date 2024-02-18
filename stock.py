import tkinter as tk
from tkinter import messagebox, ttk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_stock_info():
    symbol = entry.get().upper()
    if symbol:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            result_text.delete(1.0, tk.END)
            for key, value in info.items():
                result_text.insert(tk.END, f"{key}: {value}\n")
            
            show_graphs(stock)
            show_technical_indicators(stock)
            show_company_info(stock)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter a stock symbol.")

def show_graphs(stock):
    period = "10y"
    historical_data = stock.history(period=period)
    
    # Plotting stock price data
    fig, axs = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
    axs[0].plot(historical_data.index, historical_data['Close'], label='Close Price')
    axs[0].set_title(f"{stock.ticker} Stock Performance (Last 10 Years)")
    axs[0].set_ylabel("Close Price ($)")
    axs[0].grid(True)
    
    # Fetching and plotting dividend data
    dividends = stock.dividends
    if not dividends.empty:
        axs[1].plot(dividends.index, dividends, color='green', marker='o', linestyle='-')
        axs[1].set_ylabel("Dividends ($)")
        axs[1].grid(True)
    
    # Adding legend
    axs[0].legend()
    axs[1].legend()
    
    # Adjusting layout
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Embedding the plot in tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def show_technical_indicators(stock):
    # Example: Display moving average (50-day and 200-day)
    historical_data = stock.history(period="max")
    if len(historical_data) >= 200:  # Ensure enough data points for indicators
        ma_50 = historical_data['Close'].rolling(window=50).mean()
        ma_200 = historical_data['Close'].rolling(window=200).mean()
        
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(historical_data.index, historical_data['Close'], label='Close Price')
        ax.plot(historical_data.index, ma_50, label='50-day MA')
        ax.plot(historical_data.index, ma_200, label='200-day MA')
        ax.set_title('Technical Indicators')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price ($)')
        ax.legend()
        ax.grid(True)
        
        # Embedding the plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def show_company_info(stock):
    # Display company information
    info = stock.info
    company_info = f"Company Name: {info.get('longName', 'N/A')}\n" \
                   f"Sector: {info.get('sector', 'N/A')}\n" \
                   f"Industry: {info.get('industry', 'N/A')}\n" \
                   f"CEO: {info.get('CEO', 'N/A')}\n" \
                   f"Headquarters: {info.get('city', 'N/A')}, {info.get('country', 'N/A')}"
    company_info_text.delete(1.0, tk.END)
    company_info_text.insert(tk.END, company_info)

# Create the main window
root = tk.Tk()
root.title("Stock Market Research Application")

# Create and pack the widgets
label = tk.Label(root, text="Enter Stock Symbol:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Get Info", command=get_stock_info)
button.pack(pady=5)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=5)

company_info_text = tk.Text(root, height=6, width=50)
company_info_text.pack(pady=5)

# Run the main event loop
root.mainloop()