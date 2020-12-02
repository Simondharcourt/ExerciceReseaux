"""
    addition
"""
import random
import numpy as np
from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: implement this method
        """
        liste = []
        for p in self.peer_pool:
            liste.append(self.peer_pool[p])
        array = np.asarray(liste)

        bins_count = [0] * len(BINS)

        a = 0
        for i, b in enumerate(BINS[::-1]):

            bins_count[i] = ((array > b).sum() - a) // 2 # tous les temps étaient comptés en double.
            a = (array > b).sum()

        return np.asarray(bins_count[::-1])

class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: implement this method
        """
        result = sum(self.backend_database)

        bins_count = {}
        for i, b in enumerate(BINS):
            bins_count[b] = result[i]

        # print(bins_count)
        return bins_count


if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    # This simulation needed 11 seconds:
    # s = SimulationQ4(number_of_peers=100000, max_peer_pool_size=100)
    # s.run()
    # s.report_result()
