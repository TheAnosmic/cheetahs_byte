from unittest import TestCase

from compile import add_jmp_opcodes, break_to_atoms
from compile.jmp_add import travel, shuffle
from opcode_ import PRT


class TestJMPAdd(TestCase):
    def test_added_init_jmp(self):

        node_chain = PRT.build_from_string('u', None)
        atoms = break_to_atoms(node_chain)
        atoms = add_jmp_opcodes(atoms)
        self.assertEqual(len(atoms), 2)
        self.assertEqual(len(atoms[0]), 2)
        self.assertEqual(len(atoms[1]), 2)

    def test_nothing_happend_on_one_and_no_jmp_init(self):
        atom = PRT.build_from_string('i', None)
        atoms = break_to_atoms(atom)
        atoms = add_jmp_opcodes(
            atoms,
            first_step_is_jmp=False)
        self.assertEqual(atoms[0][0], atom[0])
        self.assertEqual(atoms[0][1], atom[1])
        self.assertEqual(len(atoms), 1)
        self.assertEqual(len(atoms[0]), 2)

    def test_first_jmp_points_to_first_node(self):
        atom = PRT.build_from_string('o', None)
        first_node = atom[0]
        atoms = break_to_atoms(atom)
        atoms = add_jmp_opcodes(atoms)
        self.assertEqual(atoms[0][0].target_uuid,
                         first_node.uuid)

    def test_reach_to_end(self):
        node_chain = PRT.build_from_string('T', None) + \
                     PRT.build_from_string('h', None) + \
                     PRT.build_from_string('e', None) + \
                     PRT.build_from_string('A', None) + \
                     PRT.build_from_string('n', None) + \
                     PRT.build_from_string('o', None) + \
                     PRT.build_from_string('s', None) + \
                     PRT.build_from_string('m', None) + \
                     PRT.build_from_string('i', None) + \
                     PRT.build_from_string('c', None)

        last = node_chain[-1]
        atoms = break_to_atoms(node_chain)
        atoms = add_jmp_opcodes(atoms)
        atom = atoms[0]
        for _ in range(len(node_chain) - 1):
            next_atom = travel(atoms, atom)
            if next_atom:
                atom = next_atom
            else:
                self.fail("Chain ended too soon")
        self.assertIn(last, atom)

    def test_reach_to_end_with_shuffle(self):
        # TODO why some are NC of NC and some NC of NODs?
        node_chain = PRT.build_from_string('T', None) + \
                     PRT.build_from_string('h', None) + \
                     PRT.build_from_string('e', None) + \
                     PRT.build_from_string('A', None) + \
                     PRT.build_from_string('n', None) + \
                     PRT.build_from_string('o', None) + \
                     PRT.build_from_string('s', None) + \
                     PRT.build_from_string('m', None) + \
                     PRT.build_from_string('i', None) + \
                     PRT.build_from_string('c', None)

        last = node_chain[-1]
        atoms = break_to_atoms(node_chain)
        atoms = add_jmp_opcodes(atoms)
        atoms = shuffle(atoms)
        atom = atoms[0]
        for _ in range(len(node_chain) - 1):
            next_atom = travel(atoms, atom)
            if next_atom:
                atom = next_atom
            else:
                self.fail("Chain ended too soon")
        self.assertIn(last, atom)
