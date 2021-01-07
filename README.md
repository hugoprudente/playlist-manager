# Playlist Manager

>[!WARNING]
>This is a work in progress...

A CLI to manage playlists and genearte playlists based on public databases.

## Example

List of examples

### Inventory

Examples for Inventory usage

#### Upsert an inventory to Google Sheets

```bash
playlist inventory spotify:playlist:4lU91kdjtDgkQxwSbPE77U
```

#### Upsert to json file only searched fields using JMESpath

as list

```bash
playtlist inventory --playlist spotify:playlist:4lU91kdjtDgkQxwSbPE77U --format value --fields "[*][track.name, track.album.name, track.album.artists[0].name]"
```

as dict

```bash
playlist inventory --playlist spotify:playlist:4lU91kdjtDgkQxwSbPE77U --format value --fields "[*].{Name: track.name, Album: track.album.name, Artist: track.album.artists[0].name}"
 ```

## Structure and Inspiration

This project is totally inspired by [dynaconf](https://github.com/rochacbruno/dynaconf). If was not for Bruno Rocha that inspires me to study Python this would never had happened, of if would it would not be public!

Thanks!!!
