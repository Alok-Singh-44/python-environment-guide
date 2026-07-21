# check_env.py
import sys

def check_virtual_environment():
    # Check if the running Python path matches the base global Python path
    is_active = sys.base_prefix != sys.prefix
    
    print("\n=============================================")
    print("🔍 VIRTUAL ENVIRONMENT DETECTOR 🔍")
    print("=============================================\n")
    
    if is_active:
        print("✅ STATUS: Virtual Environment is ACTIVE!")
        print(f"📂 Running inside sandbox: {sys.prefix}")
    else:
        print("❌ STATUS: Virtual Environment is NOT active.")
        print(f"🌍 Running globally from:  {sys.prefix}")
        
    print("\n=============================================")

if __name__ == "__main__":
    check_virtual_environment()
