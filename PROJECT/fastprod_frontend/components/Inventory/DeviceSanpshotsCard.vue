<template>
  <UiCard
    title="Devices snapshots"
    icon="content-save-cog-outline"
    :flat="false"
  >
    <template #headerActions>
      <div class="text-center">
        <v-btn
          @click="$emit('createSnapshot')"
          color="primary"
          outlined
          v-show="!loading"
        >
          Make a snapshot
        </v-btn>
        <v-btn
          @click="$emit('refresh')"
          color="primary"
          outlined
          v-show="!loading"
        >
          Refresh
        </v-btn>
      </div>
      <div class="text-center" v-show="!loading">
        <v-icon size="100" color="primary">mdi-content-save-cog-outline</v-icon>
        <br />

        <span class="text-h5 text-center" v-if="!!items">
          {{ deviceName }}
        </span>
      </div>
    </template>
    <template #content>
      <div class="text-center">
        <v-progress-circular
          :size="70"
          :width="7"
          color="primary"
          indeterminate
          v-show="loading"
        ></v-progress-circular>
      </div>
      <v-divider class="mb-4" v-show="!loading"></v-divider>

      <div v-if="!!items" v-show="!loading">
        <v-row justify="end">
          <v-col cols="4">
            <v-text-field
              v-if="items.length > 1"
              v-model="search"
              color="secondary"
              append-icon="mdi-magnify"
              label="search a snapshot..."
              single-line
              hide-details
            ></v-text-field>
          </v-col>
        </v-row>
        <v-data-table
          hide-default-footer
          class="row-pointer"
          :search="search"
          :headers="headers"
          :items="items"
          :items-per-page="100"
        >
          <template #[`item.actions`]="{ item }">
            <v-tooltip bottom>
              <template #activator="{ on, attrs }">
                <v-btn v-bind="attrs" icon v-on="on" link :href="'http://192.168.1.36:5000/snapshots/'+item.file">
                  <v-icon> mdi-cloud-download-outline </v-icon>
                </v-btn>
              </template>
              <span> Download </span>
            </v-tooltip>
          </template>
        </v-data-table>
      </div>
    </template>
  </UiCard>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      default: null,
    },
    loading: {
      type: Boolean,
      default: false,
    },
    deviceName: {
      type: String,
      default: false,
    },
  },
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Name",
          value: "file",
          align: "center",
        },
        {
          text: "Path",
          value: "path",
          align: "center",
        },
        {
          text: "At",
          value: "at",
          align: "center",
        },
        {
          text: "Actions",
          value: "actions",
          align: "center",
        },
      ],
    };
  },
  mounted() {},
  methods: {},
};
</script>
<style scoped></style>
