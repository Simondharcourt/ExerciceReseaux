from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram
import numpy as np 

class PeerQ2(Peer):

    def send_data_to_backend(self):
        """
            Question 2:
            This method should return an _array_ of the peer's
            connection durations.
        """
        liste = []
        for p in self.peer_pool:
            liste.append(self.peer_pool[p])
        return np.asarray(liste) # vecteur préféré à liste pour optimiser le stockage

class SimulationQ2(Simulation):

    def generate_network(self):
        self.network =  [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 2:
            This method should do all necessary processing to return
            the connection durations histogram bins counts.
            Don't call `plot_histogram` in this method, we just want
            to compute the histogram bins counts!
        """
        db = np.asarray(np.concatenate(self.backend_database).ravel())
        bins_count = {}

        a = 0
        for i, b in enumerate(BINS[::-1]):

            bins_count[b] = ((db > b).sum() - a) // 2 # tous les temps étaient comptés en double.
            a = (db > b).sum()


        # print(bins_count)
        return bins_count

if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()


    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    # This simulation needed 97 seconds:
    # s = SimulationQ4(number_of_peers=100000, max_peer_pool_size=100)
    # s.run()
    # s.report_result()
