{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5d3acca3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The autoreload extension is already loaded. To reload it, use:\n",
      "  %reload_ext autoreload\n"
     ]
    }
   ],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9f564df",
   "metadata": {},
   "outputs": [],
   "source": [
    "# %load \"C:\\Users\\wangj\\PycharmProjects\\statistics\\main.py\"\n",
    "# This is a sample Python script.\n",
    "\n",
    "# Press Shift+F10 to execute it or replace it with your code.\n",
    "# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.\n",
    "\n",
    "import pi_calculator\n",
    "\n",
    "def print_hi(name):\n",
    "    # Use a breakpoint in the code line below to debug your script.\n",
    "    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.\n",
    "\n",
    "def run_pi(times):\n",
    "    results={}\n",
    "    for i in times:\n",
    "        results[i]=pi_calculator.pi_calculator_np(i)\n",
    "    print(results)\n",
    "\n",
    "run_pi([10,100,1000,10000,100000,500000])\n",
    "\n",
    "# Press the green button in the gutter to run the script.\n",
    "if __name__ == '__main__':\n",
    "    print_hi('PyCharm')\n",
    "\n",
    "# See PyCharm help at https://www.jetbrains.com/help/pycharm/\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e244762",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "145ed401",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
