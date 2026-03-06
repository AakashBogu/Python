{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP3yQe93sQ49CnSeO7aFt5n",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AakashBogu/Python/blob/main/RentCalculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "tV4DMZpG2_9Q"
      },
      "outputs": [],
      "source": [
        "## Inputs need from the user\n",
        "# Total rent\n",
        "# Total food ordered\n",
        "# Electricity units spend\n",
        "# Charge per unit\n",
        "# Persons living in room/flat\n",
        "\n",
        "## Output\n",
        "# Total amount you've to pay is\n",
        "\n",
        "rent = int(input(\"Enter your hostel/flat rent = \"))\n",
        "food = int(input(\"Enter the amount of food ordered = \"))\n",
        "electricity_spend = int(input(\"Enter the total of electricity spend = \"))\n",
        "charge_per_unit = int(input(\"Enter the charge per unit = \"))\n",
        "persons = int(input(\"Enter the number of persons living in room/flat = \"))\n",
        "\n",
        "total_bill = electricity_spend * charge_per_unit\n",
        "\n",
        "output = (food + rent + total_bill) // persons\n",
        "\n",
        "print(\"Each person will pay = \", output)"
      ]
    }
  ]
}