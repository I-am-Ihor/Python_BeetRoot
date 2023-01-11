CHANNELS = ["BBC", "Discovery", "TV1000"]
INDEX_TO_NAME = dict(enumerate(CHANNELS, start=1))


class TVcontroller:
    carrent_index = 1

    def __init__(self, *args) -> None:
        self.controller = INDEX_TO_NAME

    def first_channel(self):
        """turns on the first channel from the list."""

        return self.controller[1]

    def last_channel(self):
        """turns on the last channel from the list."""

        return self.controller[len(self.controller)]

    def turn_channel(self, num_channel):
        """turns on the N channel."""

        k = self.controller.get(num_channel)
        if k == None:
            return "No such channel"
        else:
            return self.controller[num_channel]

    def next_channel(self):
        """turns on the next channel. If the current channel is the last one, turns on the first channel."""

        if self.carrent_index == len(self.controller):
            self.carrent_index = 1
        else:
            self.carrent_index += 1
        return self.controller.get(self.carrent_index)

    def previous_channel(self):
        """turns on the previous channel. If the current channel is the first one, turns on the last channel."""

        if self.carrent_index == 1:
            self.carrent_index = len(self.controller)
        else:
            self.carrent_index -= 1
        return self.controller.get(self.carrent_index)

    def current_channel(self):
        """returns the name of the current channel."""

        return self.controller.get(self.carrent_index)

    def is_exist(self, N):

        if N != "":
            for key, value in INDEX_TO_NAME.items():
                if N == value:
                    return f"Yes, number this channel is: {key}"
        else:
            return "NO"
        if N != 0:
            if N in self.controller:
                return f"Yes, name this channel is {self.controller.get(N)}"
            else:
                return "NO"


controller = TVcontroller(INDEX_TO_NAME)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(1))
print(controller.is_exist("TV1000"))
 
