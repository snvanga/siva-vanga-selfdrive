# File management in Linux

### File and Directory Management
1. **`ls`** – Lists files and directories in the current location.
2. **`cd /path/to/directory`** – Changes the working directory.
3. **`pwd`** – Prints the current working directory.
4. **`mkdir new_folder`** – Creates a new directory.
5. **`rmdir empty_folder`** – Removes an empty directory.
6. **`rm file.txt`** – Deletes a file.
7. **`rm -r folder`** – Deletes a folder and its contents.
8. **`cp file1.txt file2.txt`** – Copies a file.
9. **`cp -r dir1 dir2`** – Copies a directory recursively.
10. **`mv old_name new_name`** – Moves or renames a file or directory.

### File Viewing and Editing
11. **`cat file.txt`** – Displays file content.
12. **`tac file.txt`** – Displays file content in reverse order.
13. **`less file.txt`** – Opens a file for viewing with scrolling support.
14. **`more file.txt`** – Similar to `less`, but only moves forward.
15. **`head -n 10 file.txt`** – Displays the first 10 lines of a file.
16. **`tail -n 10 file.txt`** – Displays the last 10 lines of a file.
17. **`nano file.txt`** – Opens a simple text editor.
18. **`vi file.txt`** – Opens a powerful text editor.
19. **`echo 'Hello' > file.txt`** – Writes text to a file, overwriting existing content.
20. **`echo 'Hello' >> file.txt`** – Appends text to a file without overwriting.



# File Permissions Management in Linux

## Introduction to File Permissions
Linux file permissions determine who can read, write, or execute files and directories. Each file and directory has three levels of permission:
- **Owner (User)**: The creator of the file.
- **Group**: Users belonging to the assigned group.
- **Others**: All other users on the system.

Permissions are represented as:
- **Read (`r` or `4`)** – View file contents.
- **Write (`w` or `2`)** – Modify file contents.
- **Execute (`x` or `1`)** – Run scripts or programs.

To check file permissions, use:
```bash
ls -l filename
```
Output example:
```bash
-rwxr--r-- 1 user group 1234 Mar 28 10:00 myfile.sh
```

## Changing Permissions with `chmod`
### Using Symbolic Mode
Modify permissions using symbols:
- Add (`+`), remove (`-`), or set (`=`) permissions.

Examples:
```bash
chmod u+x filename  # Add execute for user
chmod g-w filename  # Remove write for group
chmod o=r filename  # Set read-only for others
chmod u=rwx,g=rx,o= filename  # Set full access for user, read/execute for group, and no access for others
```

### Using Numeric (Octal) Mode
Each permission has a value:
- Read (`4`), Write (`2`), Execute (`1`).

Examples:
```bash
chmod 755 filename  # User (rwx), Group (r-x), Others (r-x)
chmod 644 filename  # User (rw-), Group (r--), Others (r--)
chmod 700 filename  # User (rwx), No access for others
```

## Changing Ownership with `chown`
Modify file owner and group:
```bash
chown newuser filename  # Change owner
chown newuser:newgroup filename  # Change owner and group
chown :newgroup filename  # Change only group
```

Recursively change ownership:
```bash
chown -R newuser:newgroup directory/
```

## Changing Group Ownership with `chgrp`
```bash
chgrp newgroup filename  # Change group
chgrp -R newgroup directory/  # Change group recursively
```

## Special Permissions
### SetUID (`s` on user execute bit)
Allows users to run a file with the file owner's permissions.
```bash
chmod u+s filename
```
Example: `/usr/bin/passwd` allows users to change their passwords.

### SetGID (`s` on group execute bit)
Files: Users run the file with the group's permissions.
Directories: Files created inside inherit the group.
```bash
chmod g+s filename  # Set on file
chmod g+s directory/  # Set on directory
```

### Sticky Bit (`t` on others execute bit)
Used on directories to allow only the owner to delete their files.
```bash
chmod +t directory/
```
Example: `/tmp` directory.

## Default Permissions: `umask`
`umask` defines default permissions for new files and directories.
Check current umask:
```bash
umask
```
Set a new umask:
```bash
umask 022  # Default: 755 for directories, 644 for files
```

## Conclusion
Understanding file permissions is essential for system security and proper file management. Using `chmod`, `chown`, and `chgrp`, you can control access to files and directories efficiently.

# Linux System Monitoring

## Introduction to System Monitoring
Monitoring system resources is essential to ensure optimal performance, detect issues, and troubleshoot problems in Linux. Various tools allow us to monitor CPU, memory, disk usage, network activity, and running processes.

## Index of Commands Covered

### CPU and Memory Monitoring
- `top` – Real-time system monitoring
- `htop` – Interactive process viewer (requires installation)
- `vmstat` – Report system performance statistics
- `free -m` – Show memory usage

### Disk Monitoring
- `df -h` – Check disk space usage
- `du -sh /path` – Show disk usage of a specific directory
- `iostat` – Display CPU and disk I/O statistics

### Network Monitoring
- `ifconfig` – Show network interfaces (deprecated, use `ip a`)
- `ip a` – Show network interface details
- `netstat -tulnp` – Show active connections and listening ports
- `ss -tulnp` – Alternative to `netstat` for socket statistics
- `ping hostname` – Test network connectivity
- `traceroute hostname` – Show network path to a host
- `nslookup domain` – Get DNS resolution details

### Log Monitoring
- `tail -f /var/log/syslog` – Live monitoring of system logs
- `journalctl -f` – Live system logs for systemd-based distros
- `dmesg | tail` – View kernel logs

## CPU and Memory Monitoring
### Using `top`
To view real-time CPU and memory usage:
```bash
top
```
Press `q` to quit.

### Using `htop`
A user-friendly alternative:
```bash
htop
```
Use arrow keys to navigate and `F9` to kill processes.

### Using `vmstat`
To check CPU, memory, and I/O stats:
```bash
vmstat 1 5  # Update every 1 sec, show 5 updates
```

### Checking Memory Usage
```bash
free -m
```
Shows free and used memory in megabytes.

## Disk Monitoring
### Using `df`
Check available disk space:
```bash
df -h
```
### Using `du`
Find the size of a directory:
```bash
du -sh /var/log
```
### Using `iostat`
Check disk and CPU usage:
```bash
iostat
```

## Network Monitoring
### Checking Network Interfaces
```bash
ip a  # Show IP addresses and interfaces
```
### Viewing Open Ports and Connections
```bash
netstat -tulnp  # Show listening ports
ss -tulnp  # Alternative to netstat
```
### Testing Connectivity
```bash
ping google.com  # Test internet connection
traceroute google.com  # Trace the path to Google
```
### Checking DNS Resolution
```bash
nslookup example.com
```

## Log Monitoring
### Live Monitoring of System Logs
```bash
tail -f /var/log/syslog  # Follow logs in real-time
journalctl -f  # Systemd logs
```
### Checking Kernel Logs
```bash
dmesg | tail
```

# Disk and Storage Management in Linux

## Introduction to Disk and Storage Management
Managing disks and storage efficiently is crucial for system performance and stability. Linux provides various commands to monitor, partition, format, mount, and manage disk storage.

## Index of Commands Covered

### Viewing Disk Information
- `lsblk` – Display block devices
- `fdisk -l` – List disk partitions
- `blkid` – Show UUIDs of devices
- `df -h` – Check disk space usage
- `du -sh /path` – Show size of a directory

### Partition Management
- `fdisk /dev/sdX` – Create and manage partitions
- `parted /dev/sdX` – Alternative to `fdisk` for GPT disks
- `mkfs.ext4 /dev/sdX1` – Format a partition as ext4
- `mkfs.xfs /dev/sdX1` – Format a partition as XFS

### Mounting and Unmounting
- `mount /dev/sdX1 /mnt` – Mount a partition
- `umount /mnt` – Unmount a partition
- `mount -o remount,rw /mnt` – Remount a partition as read-write

### Logical Volume Management (LVM)
- `pvcreate /dev/sdX` – Create a physical volume
- `vgcreate vg_name /dev/sdX` – Create a volume group
- `lvcreate -L 10G -n lv_name vg_name` – Create a logical volume
- `mkfs.ext4 /dev/vg_name/lv_name` – Format an LVM partition
- `mount /dev/vg_name/lv_name /mnt` – Mount an LVM partition

### Swap Management
- `mkswap /dev/sdX` – Create a swap partition
- `swapon /dev/sdX` – Enable swap space
- `swapoff /dev/sdX` – Disable swap space

## Viewing Disk Information
### Using `lsblk`
List all block devices:
```bash
lsblk
```
### Using `fdisk`
View partition details:
```bash
fdisk -l
```
### Using `df`
Check available disk space:
```bash
df -h
```
### Using `du`
Find the size of a directory:
```bash
du -sh /var/log
```

## Partition Management
### Creating a Partition with `fdisk`
```bash
fdisk /dev/sdX
```
Follow the interactive prompts to create a partition.

### Formatting a Partition
Format as ext4:
```bash
mkfs.ext4 /dev/sdX1
```
Format as XFS:
```bash
mkfs.xfs /dev/sdX1
```

## Mounting and Unmounting
### Mount a Partition
```bash
mount /dev/sdX1 /mnt
```
### Unmount a Partition
```bash
umount /mnt
```
### Remount a Partition
```bash
mount -o remount,rw /mnt
```

## LVM Management
### Create a Physical Volume
```bash
pvcreate /dev/sdX
```
### Create a Volume Group
```bash
vgcreate vg_name /dev/sdX
```
### Create a Logical Volume
```bash
lvcreate -L 10G -n lv_name vg_name
```
### Format and Mount the Logical Volume
```bash
mkfs.ext4 /dev/vg_name/lv_name
mount /dev/vg_name/lv_name /mnt
```

## Swap Management
### Create a Swap Partition
```bash
mkswap /dev/sdX
```
### Enable Swap
```bash
swapon /dev/sdX
```
### Disable Swap
```bash
swapoff /dev/sdX
```

## Additional Notes - When to Use fdisk, mount, or Both
### Check Available Disks
Before creating or mounting anything, always check what block devices exist:
```bash
lsblk
```
### Example output:
|NAME | MAJ:MIN| RM| SIZE |RO | TYPE| MOUNTPOINT|
|-----|---------|--|------|---|-----|-----------|
|sda   |  8:0   | 0 | 100G | 0 | disk|           |
|├─sda1|   8:1  | 0 |  96G | 0 | part| /         |
|└─sda2|   8:2  | 0 |  4G  | 0 | part| [SWAP]    |
|sdb   |   8:16 | 0 |  20G | 0 | disk|           |

`sda` → existing disk (already partitioned)

`sdb` → new disk, no partitions yet

### When to use `fdisk`
Use `fdisk` when:
- The disk is brand new and has no partitions
- You want to create `/dev/sdb1`, `/dev/sdb2`, etc.

Inside `fdisk`:
1. Press `n` → create a new partition
2. Press `w` → write changes

Then confirm:
```bash
lsblk
```
### When to Use `mount`
Use `mount` when:
The partition already exists and is formatted
You just want to make it accessible
```bash
sudo mkdir /mnt/mydisk
sudo mount /dev/sdb1 /mnt/mydisk
```
Now your disk is available at `/mnt/mydisk`.

### When to Use fdisk + mount (Full Setup)
Use `fdisk + mkfs + mount` when:
The disk is completely new
You need to partition → format → mount it
```bash
# 1. Check available disks
lsblk
# 2. Create partition
sudo fdisk /dev/sdb
# 3. Format the partition
sudo mkfs.ext4 /dev/sdb1
# 4. Mount it
sudo mkdir /data
sudo mount /dev/sdb1 /data
```
### Quick Reference

| Use Case                     | Command(s)                  |
|-------------------------------|-----------------------------|
| View disks and partitions     | `lsblk`                     |
| Partition a new disk          | `fdisk`                     |
| Mount an existing partition   | `mount`                     |
| Full setup (new disk)         | `fdisk + mkfs + mount`      |