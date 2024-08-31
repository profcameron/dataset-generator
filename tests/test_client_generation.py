import unittest
import re
import data_generator

# Test suite for data_generator
class TestClientTableGeneration(unittest.TestCase):
    def test_generate_client_table(self):
        size = 10
        result = data_generator.generate_client_table(size)
        self.assertIn(f"ClientNum CHAR({size + 1})", result)

    # Test that the generate_email function generates an email with an @ and a .
    def test_generate_email(self):
        first_name = "John"
        last_name = "Doe"
        email = data_generator.generate_email(first_name, last_name)
        self.assertIn("@", email, "Email is missing an @")
        self.assertIn(".", email, "Email is missing a period.")

    # Test that the generate_id generates an ID following rules
    def test_generate_id(self):
        id_size = 5
        value = 123
        result = data_generator.generate_id(id_size, value)
        self.assertEqual(len(result), id_size + 1, "Size of ID is incorrect")  # +1 for the 'C' prefix
        self.assertEqual(result[0], 'C', "ID does not start with C")
        self.assertEqual(result, 'C00123', "Generated ID is incorrect")

    # Test the generate_phone generates something that is a valid phone number
    def test_generate_phone(self):
        phone_number = data_generator.generate_phone()
        # length of returned value should be 12
        self.assertEqual(len(phone_number), 12)  # XXX-XXX-XXXX
        # Pattern for XXX-XXX-XXXX
        expected_phone_regex = r"^\d{3}-\d{3}-\d{4}$"  
        self.assertTrue(re.match(expected_phone_regex, phone_number), "Phone number is not in the format XXX-XXX-XXXX")

    # Test that the generate_record creates an insert that matches the expected pattern
    def test_generate_record(self):
        key = "C12345"
        last = "Doe"
        first = "John"
        street_num = "123"
        street_name = "Main"
        street_type = "St"
        city = "Beverly Hills"
        state = "CA"
        zip = "90210"
        record = data_generator.generate_record(key, last, first, street_num, street_name, street_type, city, state, zip)
        self.assertIn(key, record)
        self.assertIn(last, record)
        self.assertIn(first, record)
        self.assertIn(street_num, record)
        self.assertIn(street_name, record)
        self.assertIn(street_type, record)
        self.assertIn(city, record)
        self.assertIn(state, record)
        self.assertIn(zip, record)

    def test_generate_email_length(self):
        first_name = "John"
        last_name = "Doe"
        email = data_generator.generate_email(first_name, last_name)
        self.assertLessEqual(len(email), 75)  # Email field length in the database

    def test_generate_phone_format(self):
        phone_number = data_generator.generate_phone()
        parts = phone_number.split("-")
        self.assertEqual(len(parts), 3)
        self.assertEqual(len(parts[0]), 3)
        self.assertEqual(len(parts[1]), 3)
        self.assertEqual(len(parts[2]), 4)

if __name__ == '__main__':
    unittest.main()