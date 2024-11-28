import os
import hashlib
from collections import defaultdict
from pathlib import Path
import argparse

def calculate_file_hash(filepath, hash_algorithm='md5', buffer_size=8192):
    """
    Calculate hash of a file using specified algorithm.
    
    Args:
        filepath (str): Path to the file
        hash_algorithm (str): Hash algorithm to use ('md5', 'sha256', etc.)
        buffer_size (int): Size of chunks to read from file
    
    Returns:
        str: Hexadecimal hash of the file
    """
    hash_func = getattr(hashlib, hash_algorithm)()
    
    try:
        with open(filepath, 'rb') as file:
            while chunk := file.read(buffer_size):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except (IOError, OSError) as e:
        print(f"Error reading file {filepath}: {e}")
        return None

def find_duplicate_files(folder_path, hash_algorithm='md5'):
    """
    Find duplicate files in the specified folder and its subfolders.
    
    Args:
        folder_path (str): Path to the folder to search
        hash_algorithm (str): Hash algorithm to use for file comparison
    
    Returns:
        dict: Dictionary with hashes as keys and lists of duplicate file paths as values
    """
    # Use defaultdict to automatically create lists for new hash values
    hash_map = defaultdict(list)
    folder_path = Path(folder_path)
    
    try:
        # Walk through directory tree
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                full_path = Path(dirpath) / filename
                
                # Skip files that can't be accessed
                if not os.access(full_path, os.R_OK):
                    print(f"Warning: Cannot access file {full_path}")
                    continue
                    
                # Calculate file hash
                file_hash = calculate_file_hash(full_path, hash_algorithm)
                if file_hash:
                    hash_map[file_hash].append(full_path)
                    
        # Filter out unique files
        return {k: v for k, v in hash_map.items() if len(v) > 1}
        
    except Exception as e:
        print(f"Error processing directory {folder_path}: {e}")
        return {}

def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='Find duplicate files in a directory')
    parser.add_argument('folder', help='Folder to search for duplicates')
    parser.add_argument('--algorithm', choices=['md5', 'sha256', 'sha1'], 
                        default='md5', help='Hash algorithm to use')
    args = parser.parse_args()
    
    # Find duplicates
    duplicate_files = find_duplicate_files(args.folder, args.algorithm)
    
    # Print results
    if not duplicate_files:
        print("No duplicate files found.")
        return
        
    print("\nDuplicate files found:")
    for hash_value, file_list in duplicate_files.items():
        print(f"\nFiles with hash {hash_value}:")
        for file_path in file_list:
            print(f"  {file_path}")
        print(f"Total size: {os.path.getsize(file_list[0])} bytes")

if __name__ == "__main__":
    main()
