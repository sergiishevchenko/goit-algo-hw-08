import heapq

from generate_random_cables import generate_random_cables


def get_min_cost(data):
    return min(data)


def count_sum_of_costs(data):
    return sum(data)


def main(cables):
    # Transform cables list into a heap
    heapq.heapify(cables)

    # cable costs list
    cable_costs = []

    while len(cables) > 1:
        # Pop the smallest item off the heap.
        smallest_cable_cost_1 = heapq.heappop(cables)
        # Pop the smallest item off the heap.
        smallest_cable_cost_2 = heapq.heappop(cables)
        # sum of two smallest cable costs
        total_costs = smallest_cable_cost_1 + smallest_cable_cost_2

        cable_costs.append(total_costs)

        # Push item onto heap
        heapq.heappush(cables, total_costs)

    return cable_costs


if __name__ == '__main__':
    get_min_cost(main(generate_random_cables(50)))
    count_sum_of_costs(main(generate_random_cables(50)))