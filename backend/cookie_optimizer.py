from sklearn.cluster import KMeans
import numpy as np
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

class CookieOptimizer:
    def __init__(self, tray_width: float, tray_height: float):
        self.tray_width = tray_width
        self.tray_height = tray_height

    def calculate_grid_size(self, cookie_diameter: float):
        """Calculate available positions considering cookie size"""
        effective_width = self.tray_width - cookie_diameter
        effective_height = self.tray_height - cookie_diameter
        
        # Use cookie diameter as minimum spacing
        x_positions = max(2, int(effective_width / (cookie_diameter/2)))
        y_positions = max(2, int(effective_height / (cookie_diameter/2)))
        
        return x_positions, y_positions

    def optimize_positions(self, cookie_diameter: float, num_cookies: int, max_attempts=100):
        x_positions, y_positions = self.calculate_grid_size(cookie_diameter)
        
        best_positions = None
        max_min_distance = 0
        
        for _ in range(max_attempts):
            x = np.linspace(cookie_diameter/2, self.tray_width - cookie_diameter/2, x_positions)
            y = np.linspace(cookie_diameter/2, self.tray_height - cookie_diameter/2, y_positions)
            xx, yy = np.meshgrid(x, y)
            grid_positions = np.column_stack((xx.ravel(), yy.ravel()))
            
            kmeans = KMeans(n_clusters=num_cookies, random_state=0)
            kmeans.fit(grid_positions)
            current_positions = kmeans.cluster_centers_
            
            distances = pdist(current_positions)
            min_distance = np.min(distances) if len(distances) > 0 else 0
            
            if min_distance >= cookie_diameter and min_distance > max_min_distance:
                max_min_distance = min_distance
                best_positions = current_positions.copy()
        
        if best_positions is None:
            raise ValueError("Could not find valid positions without collisions")
        
        best_positions = np.round(best_positions, 2)
        max_min_distance = round(max_min_distance, 2)

        return best_positions.tolist(), max_min_distance

    def visualize_positions(self, positions, cookie_diameter, min_distance):
        fig, ax = plt.subplots(figsize=(len(positions), len(positions)))
        ax.set_xlim(0, self.tray_width)
        ax.set_ylim(0, self.tray_height)
        ax.set_aspect('equal')
        
        # Draw safe zones
        for x, y in positions:
            safe_zone = plt.Circle((x, y), cookie_diameter * 0.6, fill=True, alpha=0.1, color='red')
            cookie = plt.Circle((x, y), cookie_diameter/2, fill=False)
            ax.add_artist(safe_zone)
            ax.add_artist(cookie)
        
        plt.title(f'Cookie Positions\nMinimum distance between centers: {min_distance:.2f} cm')
        plt.xlabel('Width (cm)')
        plt.ylabel('Height (cm)')
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    optimizer = CookieOptimizer(30, 40)
    positions, min_distance = optimizer.optimize_positions(cookie_diameter=10, num_cookies=5)
    optimizer.visualize_positions(positions, 10, min_distance)